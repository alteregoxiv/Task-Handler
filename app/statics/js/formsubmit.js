"rgba(240, 0, 0, 0.1) none repeat scroll 0% 0%"
"rgba(0, 0, 0, 0) none repeat scroll 0% 0%"

function signinSubmit(form){

    u = form.elements[0];
    p = form.elements[1];

    if(u.value==""){
        showWarning(
                u , 
                document.getElementById("invalid-username"),
                "Username Required"
            );
        return false;
    }

    if(p.value=""){
        showWarning(
            u , 
            document.getElementById("invalid-password"),
            "Password Required"
        );
        return false;
    }

}

function signupSubmit(form){

    u = form.elements[0];
    e = form.elements[1];

    if(u.value==""){
        showWarning(
                u , 
                document.getElementById("invalid-user"),
                "Username Required"
            );
            return false;
    }

    if(e.value=""){
        showWarning(
            u , 
            document.getElementById("invalid-email"),
            "E-Mail Required"
        );
        return false;
        }

}