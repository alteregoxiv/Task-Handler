resendPassword = (function() {
        let count = 2;
        return function(form) {
                emailId = form.elements['email'].value
                fetch('/resend-password?email=' + emailId)
                        .then(function(data) { return data.json(); })
                        .then(function(data) {
                                form.elements['hash'].value = data['hash'];
                                if (count > 0) {
                                        count--;
                                        let button = form.elements[5];
                                        button.innerHTML = `Resend(${count})`;
                                }
                                if (count === 0) button.disabled = true;
                        })
                        .catch(function(err) { throw err; })
                
        }
})();
