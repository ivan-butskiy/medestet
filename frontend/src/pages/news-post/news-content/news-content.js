import React, { Component } from 'react';
import ReactHtmlParser from 'react-html-parser';

import './news-content.css';

class NewsContent extends Component {

    state = {
        text: ''
    };

    componentDidMount() {
        this.setState({ text: this.props.text })
    };

    componentDidUpdate(prevProps) {
        if (this.props !== prevProps) {
            this.setState({ text: this.props.text })
        };
    };

    render() {

        const { text } = this.state

        return (
            <div className='card blog-content shadow-sm'>
                { ReactHtmlParser(text) }
            </div>
        );
    };
};

export default NewsContent;
