import React, { Component } from 'react';

import './option-item.css';

class OptionItem extends Component {

    state = {
        title: this.props.title,
        description: this.props.description,
        price: this.props.price
    }

    render() {

        const { title, description, price } = this.state;

        return (

            <div className='col-lg-4 mb-5 mb-lg-0 option-item'>
                <div className='bg-white p-5 rounded-lg shadow option-item-detail'>
                    <h4 className='h5 mb-4'>{ title }</h4>

                    <p><i className='fas fa-tags mr-2'></i>Стоимость: { price } грн.</p>

                    <div className='custom-separator my-4 mx-auto bg-primary description'></div>                                
                        { description }
                </div>
            </div>

        );
    };
};

export default OptionItem;