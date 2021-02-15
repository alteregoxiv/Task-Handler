
function validatePassword(self){

    if(self.value !== ""){

        hideWarning(

            self,
            document.getElementById("invalid-password")

        );

    }

}


function signinSubmit(form){

    u = form.elements[0];
    p = form.elements[1];

    if(u.style.background.includes("rgba(240, 0, 0, 0.1)"))
        return false;

    if(u.value===""){
        showWarning(
                u , 
                document.getElementById("invalid-username"),
                "Username Required"
            );
        return false;
    }

    if(p.value===""){
        showWarning(
            p , 
            document.getElementById("invalid-password"),
            "Password Required"
        );
        return false;
    }

    form.submit();

}

function signupSubmit(form){

    u = form.elements[0];
    e = form.elements[1];

    if(u.value===""){
        showWarning(
                u , 
                document.getElementById("invalid-user"),
                "Username Required"
            );
            return false;
    }

    if(e.value===""){
        showWarning(
            e , 
            document.getElementById("invalid-email"),
            "E-Mail Required"
        );
        return false;
    }

    if(u.style.background.includes("rgba(0, 255, 0, 0.1)") && e.style.background.includes("rgba(0, 255, 0, 0.1)"))
        form.submit();


}


document.addEventListener('keypress', function(event) {
        if (event.keyCode !== 13)
                return;
        let button = document.getElementsByTagName('button');
        if (button[0].parentElement.parentElement.classList.contains('active'))
                button[0].click();
        else
                button[1].click();
})
