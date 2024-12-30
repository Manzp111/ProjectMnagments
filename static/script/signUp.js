const form = document.getElementById('form');
const username = document.getElementById('username');
const email = document.getElementById('email');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');
const date = document.getElementById('date');
const phone=document.getElementById('phone');
const firstNmae=document.getElementById('firstNmae');
const lastName=document.getElementById('lastName');


form.addEventListener('submit', e => {
	e.preventDefault();

	checkInputs();
});

function checkInputs() {
	// trim to remove the whitespaces
	const usernameValue = username.value.trim();
	const emailValue = email.value.trim();
	const passwordValue = password.value.trim();
	const password2Value = password2.value.trim();
	const dateValue=date.value.trim();
	const phoneValue=phone.value.trim();
	const firstNmaeValue=firstNmae.value.trim();
	const lastNameValue = lastName.value.trim();

	if(lastNameValue===''){
		setErrorFor(lastName,'write your last name')
	}

	if (firstNmaeValue===''){
		setErrorFor(firstNmae,'write your name')
	}

	if(phoneValue===''){
		setErrorFor(phone,'phone number can not be blank')
	}
	if(dateValue==='')

	{
		setErrorFor( date,'date cant be blank')
	}

	if(usernameValue === '') {
		setErrorFor(username, 'Username cannot be blank');
	}
	if(emailValue === '') {
		setErrorFor(email, 'Email cannot be blank');
	}
	else if (!isEmail(emailValue)) {
		setErrorFor(email, 'Not a valid email');
	}

	if(passwordValue === '') {
		setErrorFor(password, 'Password cannot be blank');
	}
	if(password2Value === '') {
		setErrorFor(password2, 'Password2 cannot be blank');
	} else if(passwordValue !== password2Value) {
		setErrorFor(password2, 'Passwords does not match');
	} else{
		setSuccessFor(password2);
	}
}

function setErrorFor(input, message) {
	const formControl = input.parentElement;
	const small = formControl.querySelector('small');
	formControl.className = 'form-control error';
	small.innerText = message;
}

function isEmail(email) {
	return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}