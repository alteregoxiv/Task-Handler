function validateSignUpUserName(self) {
        
        if (!validateUserName(self, "invalid-user"))
                return;

        let warning = document.getElementById('invalid-user')
        if (self.value === '') {
                hideWarning(self, warning)
                return;
        }

        console.log(self.style.background)
        if(self.style.background.includes("rgba(0, 255, 0, 0.1)"))
                alert('yo');

        let spinner = document.getElementsByClassName('spinner-grow')[0];
        spinner.style.display = 'inline-block';
        fetch("/validate?username=" + self.value)
                .then(function(data) {
                        return data.json();
                })
                .then(function(data) {
                        if (data.valid === "invalid")
                                showWarning(
                                        self,
                                        warning,
                                        "Username not available"
                                );
                        else 
                                showSuccess(self);
                        spinner.style.display = 'none';
                })
                .catch(function(err) {
                        throw err;
                })
}


function validateEmail(self) {

        if (!document.getElementsByTagName('form')[1].reportValidity())
                return;

        let warning = document.getElementById('invalid-email')
        if (self.value === '') {
                hideWarning(self, warning)
                return;
        }

        if(self.style.background.includes("rgba(0, 255, 0, 0.1)"))
                return;

        let spinner = document.getElementsByClassName('spinner-grow')[1];
        spinner.style.display = 'inline-block';
        fetch("/validate?email=" + self.value)
                .then(function(data) {
                        return data.json();
                })
                .then(function(data) {
                        if (data.valid === "invalid")
                                showWarning(
                                        self,
                                        warning,
                                        "Email already registered"
                                );
                        else 
                                showSuccess(self);
                        spinner.style.display = 'none';
                })
                .catch(function(err) {
                        throw err;
                })
}


function validateUserName(self, id) {
        warning = document.getElementById(id)
        if (self.value.split(' ').length > 1) {
                showWarning(self, warning, 'Username should be a single word');
                return false;
        }
        self.style.background.includes('rgba(0, 255, 0, 0.1)')
                ? "": hideWarning(self, warning);
        return true;
}


function showWarning(self, warning, message) {
        self.style.border = "2px solid red";
        self.style.background = "rgba(240, 0, 0, .1)";
        warning.innerHTML = message; 
}


function hideWarning(self, warning) {
        self.style.border = "1px solid black";
        self.style.background = "none";
        warning.innerHTML = '';
} 

function showSuccess(self) {
        self.style.border = "2px solid #0f0";
        self.style.background = "rgba(0, 255, 0, .1)";
}
