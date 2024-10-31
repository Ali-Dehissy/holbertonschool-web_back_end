import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 0 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

/* Redis Client and Utilities */
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

function reserveStockById(itemId, stock) {
  client.set(itemId, stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(itemId);
  return stock ? parseInt(stock, 10) : 0;
}

/* Helper Functions */
function getItemById(id) {
  return listProducts.find((item) => item.itemId === id);
}

/* Express Server */
const app = express();
app.listen(1245, () => {
  listProducts.forEach((product) => reserveStockById(product.itemId, product.initialAvailableQuantity));
  console.log('Server is running on port 1245');
});

/* Endpoints */
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);

  if (item) {
    const stock = await getCurrentReservedStockById(itemId);
    res.json({ ...item, currentQuantity: stock });
  } else {
    res.status(404).json({ status: 'Product not found' });
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    res.status(404).json({ status: 'Product not found' });
    return;
  }

  const stock = await getCurrentReservedStockById(itemId);

  if (stock < 1) {
    res.status(403).json({ status: 'Not enough stock available', itemId });
  } else {
    reserveStockById(itemId, stock - 1);
    res.json({ status: 'Reservation confirmed', itemId });
  }
});
