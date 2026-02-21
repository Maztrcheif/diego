const username = document.getElementById("username")
const password = document.getElementById("password")
const login_btn = document.getElementById("login")
const create_btn = document.getElementById("create")

function login(username,password) {
    user = username.value
    pass = password.value
    console.log(pass,user)
}
function create() {

}

login_btn.addEventListener("click", () => login(username,password)) 
 