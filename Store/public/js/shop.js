const products = [
    {id: 1, name: "Banana", category:"produce", price: 1.99},
    {id: 2, name: "Apple", category:"produce", price: 1.49},
    {id: 3, name: "Concha", category: "bakery", price: .99},
    {id: 4, name: "Donut", category: "bakery", price: .99},
    {id: 5, name: "Beef", category: "meat", price: 5.99},
    {id: 6, name: "Chicken", category: "meat", price: 4.99},
    {id: 7, name: "Rice", category: "grocery", price: 2.99}
]
const productgrid = document.getElementById("products")
const searchbar = document.getElementById("search")
const categoryselect = document.getElementById("category")


const renderproducts = (items) => {
    productgrid.innerHTML = ""
    items.forEach(product => {
        const div = document.createElement("div")
        div.classList.add("product")
        div.innerHTML = `
                <div>
                    <h3>${product.name}</h3>
                    <p>Category: ${product.category}</p>
                </div>
                <div>
                    <p>Price: ${product.price.toFixed(2)}</p>
                    <button class="buy">Add to Cart</button>
                </div>
            `
            productgrid.appendChild(div)
    });

}
 renderproducts(products)

 const filterProducts = () => {
    const searchTerm = searchbar.value.toLowerCase()
    const category = categoryselect.value
    const filtered = products.filter (product => {
        const sameName = product.name.toLowerCase().includes(searchTerm)
        const sameCategory = category === "all" ? true : product.category === category
        return sameName && sameCategory
 })
 renderproducts(filtered)
 }
 
 searchbar.addEventListener("input", filterProducts)
 categoryselect.addEventListener("change", filterProducts)
 productgrid.addEventListener()