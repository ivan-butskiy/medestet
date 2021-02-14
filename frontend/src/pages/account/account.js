import React, { Component } from 'react';
import { connect } from 'react-redux';
import NonAuth from '../non-auth';

import './account.css';

import HeaderAccount from './header-account';
import PersonalData from './components/personal-data';
import ChangePassword from './components/change-password';
import Certify from './components/certify';
import Courses from './components/courses';
import Webinars from './components/webinars';

class Account extends Component {

    render() {

        if (!this.props.isAuthenticated) {
            return <NonAuth />
        };

        return (
            <div className='account shadow-lg justify-content-center p-2'>
                <HeaderAccount
                    firstName={ this.props.firstName }
                    lastName={ this.props.lastName }
                    photo={ this.props.photo }
                    buyCount={ this.props.buyCount }
                    buySum={ this.props.buySum }
                />
                <div className='profile container-fluid'>
                    <div className='row justify-content-center'>
                        <Courses />
                        <Webinars />
                        <PersonalData />
                        <ChangePassword />
                        <Certify />
                    </div>
                </div>
            </div>
        );
    };
};

const mapStateToProps = store => ({
    isAuthenticated: store.authReducer.isAuthenticated,
    firstName: store.authReducer.firstName,
    lastName: store.authReducer.lastName,
    photo: store.authReducer.photo,
    buySum: store.authReducer.buySum,
    buyCount: store.authReducer.buyCount,
});

export default connect(mapStateToProps, null)(Account);