
function result() {
    const res = fetch('https://djangoapi.up.railway.app/api/v1/students/')
    console.log(res.json)
}
result()

console.log("object");