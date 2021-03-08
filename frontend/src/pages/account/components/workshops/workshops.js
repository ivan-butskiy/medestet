import React, { Component } from 'react';
import { Link } from 'react-router-dom';

import './workshops.css';

class Workshops extends Component {

    render() {

        return (
            <div className='personal-data col-sm-6 col-md-4 text-center'>
                <div className='card shadow-sm p-3'>
                    <i className='fas fa-user-friends'></i>
                    <Link to='/account/workshops/'>Мои семинары</Link>
                </div>
            </div>
        );
    };
};

export default Workshops;