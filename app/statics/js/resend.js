resendPassword = (function() {
        let count = 2;
        return function(form) {
                if (count > 0) {
                        emailId = form.elements['email'].value
                        fetch('/resend-password?email=' + emailId)
                                .then(function(data) { return data.json(); })
                                .then(function(data) {
                                        form.elements['hash'].value = data['hash'];
                                        let button = form.elements[5];
                                        count--;
                                        button.innerHTML = `Resend(${count})`;
                                        if (count === 0) button.disabled = true;
                                })
                                .catch(function(err) { throw err; })
                }
        }
})();
