import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Redirect } from 'react-router-dom';

import { signUp } from '../../actions/auth';

import './register.css';

class Register extends Component {

    state = {
        email: '', 
        firstName: '', 
        lastName: '', 
        password: '', 
        rePassword: '',

        passwordNotMatching: null,
        passwordLength: null,
        emailIncorrect: null,
        error: null,
        success: null
    };

    onChangeHandler(e) {
        this.setState({
            [e.target.name]: e.target.value,
            passwordLength: false,
            passwordNotMatching: false,
            error: false
        });
    };

    onSubmitHandler(e) {
        e.preventDefault();
        
        const { email, firstName, lastName, password, rePassword } = this.state;

        if (password.length <= 6) {
            this.setState({ passwordLength: true });
        } else if (password !== rePassword) {
            this.setState({ passwordNotMatching: true});
        } else {
            this.props.signUp(email, firstName, lastName, password, rePassword)
                .then(result => {
                    if (!result.data) {
                        this.setState({ error: true })
                    } else {
                        this.setState({ success: true })
                    }
                });
        };
    };

    render() {

        if (this.props.isAuthenticated) {
            return (
                <Redirect to='/' />
            );
        };

        if (this.state.success) {
            return (
                <Redirect to='/' />
            )
        }

        const { 
                email, 
                firstName, 
                lastName, 
                password, 
                rePassword, 
                passwordNotMatching,
                passwordLength,
                error } = this.state;

        return (
            <div className='jumbotron container shadow-lg register'>
                <h1 className='display-4'>Регистрация</h1>
                <p className='mt-4'>Зарегистрируйтесь на сайте, чтобы иметь возможность проходить курсы, подтвердить статус косметолога сертификатом и покупать товары в нашем интернет-магазине.</p>
                <hr className='my-4' />

                { error ? <div className='alert alert-danger' role='alert'>
                Ошибка в регистрации. Возможно, пользователь с таким e-mail уже существует.
                Проверьте правильность введенных данных и повторите попытку.
                </div> : null }

                { passwordNotMatching ? <div className='alert alert-danger' role='alert'>
                Введенные пароли не совпадают.
                </div> : null }

                { passwordLength ? <div className='alert alert-danger' role='alert'>
                Длина пароля должна быть больше 6 символов.
                </div> : null }



                <form onSubmit={ (e) => this.onSubmitHandler(e) }>
                    <div className='row'>

                        <div className='col-md-6'>
                            <div className='form-group'>
                                <label htmlFor='exampleInputEmail1'>Email</label>
                                <input 
                                    type='email'
                                    name='email'
                                    className='form-control' 
                                    id='exampleInputEmail1' 
                                    aria-describedby='emailHelp'
                                    onChange={ (e) => this.onChangeHandler(e) }
                                    value={ email }
                                    required />
                            </div>
                            <div className='form-group'>
                                <label htmlFor='firstName'>Имя</label>
                                <input 
                                    type='text'
                                    name='firstName'
                                    className='form-control' 
                                    id='firstName'
                                    onChange={ (e) => this.onChangeHandler(e) }
                                    value={ firstName }
                                    required />
                            </div>
                            <div className='form-group'>
                                <label htmlFor='lastName'>Фамилия</label>
                                <input 
                                    type='text'
                                    name='lastName'
                                    className='form-control' 
                                    id='lastName'
                                    onChange={ (e) => this.onChangeHandler(e) }
                                    value={ lastName }
                                    required />
                            </div>
                        </div>

                        <div className='col-md-6'>
                            <div className='form-group'>
                                <label htmlFor='password'>Пароль</label>
                                <input 
                                    type='password'
                                    name='password'
                                    className='form-control' 
                                    id='password'
                                    onChange={ (e) => this.onChangeHandler(e) }
                                    value={ password }
                                    required />
                            </div>
                            <div className='form-group'>
                                <label htmlFor='rePassword'>Повторите пароль</label>
                                <input 
                                    type='password'
                                    name='rePassword'
                                    className='form-control' 
                                    id='rePassword'
                                    onChange={ (e) => this.onChangeHandler(e) }
                                    value={ rePassword }
                                    required />
                            </div>
                            <button type='submit' className='btn btn-primary'>Регистрация</button>
                        </div>

                    </div>
                </form>
            </div>
        );
    };
};

const mapStateToProps = (store) => ({
    isAuthenticated: store.authReducer.isAuthenticated
});

export default connect(mapStateToProps, { signUp })(Register);