function goHomePage(){
    window.location.href = homeLink;
}

function signUpValidation(){

    let userName = document.getElementById("userNameView");

    if(userName.value.length < 3){
        alert("Username must has length greater than 3 characters");
        return false;
    }

    let pass = document.getElementById("passView");
    let confirmPass = document.getElementById("confirmView");

    if(pass.value.length < 6){
        alert("Password must has length greater than 6 characters");
        return false;
    }

    if(pass.value !== confirmPass.value){
        alert("Password does not match with confirmation one, please make sure they are the same");
        return false;
    }

    return true;

}