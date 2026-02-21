async function fetchProducts() {
    try {
        const response = await fetch('api/get_products.php')
        const products = await response.json()
        return products
    } catch (error) {
        console.error('Error fetching products', error)
        return []
        
    }
    
}

const productgrid = document.getElementById("products")
const searchbar = document.getElementById("search")
const categoryselect = document.getElementById("category")

fetchProducts().then(products => {
    renderproducts(products)
    searchbar.addEventListener("input", () => filterProducts(products))
    categoryselect.addEventListener("change", () => filterProducts(products))
})



function renderproducts(items) {
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


 

 function filterProducts(products) {
    const searchTerm = searchbar.value.toLowerCase()
    const category = categoryselect.value
    const filtered = products.filter(product => {
        const sameName = product.name.toLowerCase().includes(searchTerm)
        let sameCategory = product.category == category
        if (category == "all") {
             sameCategory = true
        }
 //           const sameCategory = category === "all" ? true : product.category === category
        return sameName && sameCategory
 })
 renderproducts(filtered)
 }
 
 
 productgrid.addEventListener("click", (event) => {
    const button = event.target.closest(".buy")
    if (!button) return
    const product = button.closest(".product")
    const name = product.querySelector("h3").textContent
    console.log("added to cart", name)
 })

 