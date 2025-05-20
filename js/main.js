const API_URL = 'http://127.0.0.1:5000/students';

const form = document.getElementById('studentForm');
const nameInput = document.getElementById('nombre');
const last_nameInput = document.getElementById('apellido');
const programa_academicoInput = document.getElementById('programa_academico');
const edadInput = document.getElementById('edad');
const studentsList = document.getElementById('studentsList');

async function loadStudents() {
  const response = await fetch(API_URL);
  const students = await response.json();
  studentsList.innerHTML = '';

  students.forEach(({ id, nombre, apellido, programa_academico, edad }) => {
    const li = document.createElement('li');
    li.innerHTML = `
      <strong>Estudiante: ${nombre}, ${apellido}</strong>,edad: ${edad}. Programa academico: ${programa_academico}.
    `;
    studentsList.appendChild(li);
  });
}

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const newStudent = {
    nombre: nameInput.value,
    apellido: last_nameInput.value,
    programa_academico: programa_academicoInput.value,
    edad: edadInput.value
  };

  const response = await fetch(API_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(newStudent)
  });

  if (response.ok) {
    alert('Estudiante creado exitosamente');
    form.reset();
    loadStudents();
  } else {
    alert('Error al crear un Estudiante');
  }
});

loadStudents();