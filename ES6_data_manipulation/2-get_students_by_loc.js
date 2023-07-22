function getStudentsByLocation(students, city) {
  if (!Array.isArray(students)) {
    return [];
  }

  const results = students.filter((item) => item.location === city);

  return results;
}

export default getStudentsByLocation;
