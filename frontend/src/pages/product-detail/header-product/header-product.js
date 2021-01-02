import React, { Component } from 'react';

import './header-product.css';

class HeaderProduct extends Component {

    render() {

        return (
            <div 
                className='jumbotron jumbotron-fluid shadow-sm header-shop'>
                <div className='container'>
                    <h1 className='display-4'>Интернет-магазин компании MedEstet</h1>
                </div>
            </div>
        );
    };
};

export default HeaderProduct;