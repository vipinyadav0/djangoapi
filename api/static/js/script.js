async function getData() {
    const response = await fetch('https://djangoapi.up.railway.app/api/v1/students/');
    const data = await response.json();
    console.log(data);
}

getData()
console.log("object");