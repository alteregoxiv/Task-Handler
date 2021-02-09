function validateSignUpUserName(self) {
        
        if (!validateUserName(self, "invalid-user"))
                return;
}


function validateEmail(self) {

}


function validateUserName(self, id) {
        warning = document.getElementById(id)
        if (self.value.split(' ').length > 1) {
                showWarning(self, warning)
                return false
        }
        hideWarning(self, warning)
        return true;
}


function showWarning(self, warning) {
        self.style.border = "2px solid red";
        self.style.background = "rgba(240, 0, 0, .1)"
        warning.innerHTML = 'username should be a single word';
}


function hideWarning(self, warning) {
        self.style.border = "1px solid black";
        self.style.background = "none"
        warning.innerHTML = '';
} 
