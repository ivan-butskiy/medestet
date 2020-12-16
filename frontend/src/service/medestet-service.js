import axios from 'axios';

class MedestetService {

    API_BASE = 'http://localhost:8000';

    config = {
        headers: {
            'Content-Type': 'application/json'
        }
    };

    getResource = async (url, ...args) => {
        const response = await axios.get(`${this.API_BASE}${url}`, this.config);
        if (!response.status === 200) {
            throw new Error('Could not axios url.');
        };
        return await response;
    };

    getCoursesList = () => {
        const result = this.getResource('/api/courses/');
        return result;
    };

    getCourseDetail = (slug) => {
        const result = this.getResource(`/api/courses/${slug}/`);
        return result;
    };

    getWorkshopsList = () => {
        const result = this.getResource('/api/workshops/');
        return result;
    };

    getWorkshopDetail = (slug) => {
        const result = this.getResource(`/api/workshops/${slug}/`);
        return result;
    };

    getWebinarsList = () => {
        const result = this.getResource('/api/webinars/');
        return result;
    };

    getWebinarDetail = (slug) => {
        const result = this.getResource(`/api/webinars/${slug}/`);
        return result;
    };

};

export default MedestetService;

// TODO добавить JWT в авторизацию и протестировать