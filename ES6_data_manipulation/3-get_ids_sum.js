export default function getStudentIdsSum(student) {
	return student.reduce((acc, student) => acc + student.id, 0);
}
