function myComponent() {
    let state = {};

    function setState(newState) {
        state = { ...state, ...newState };
    }

}


async function getData() {
    const response = await fetch('https://djangoapi.up.railway.app/api/v1/students/');
    const data = await response.json();
    data.map((e, id) => {
        myComponent()
    })
}
getData()