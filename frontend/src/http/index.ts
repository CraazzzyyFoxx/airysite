import axios from "axios";
import {AuthResponse} from "../models/response/AuthResponse";
import {API_URL} from "../consts/API";
var JSONbig = require('json-bigint')

const $api = axios.create({
    withCredentials: true,
    baseURL: API_URL
})

$api.interceptors.request.use((config) => {
    // @ts-ignore
    config.headers.Authorization = `Bearer ${localStorage.getItem('token')}`;
    config.transformResponse = data => JSONbig.parse(data);
    return config;
})


$api.interceptors.response.use((config) => {
    return config;
},async (error) => {
    const originalRequest = error.config;

    if (error.response.status == 401 && error.config && !error.config._isRetry) {
        originalRequest._isRetry = true;
        try {
            const response = await axios.get<AuthResponse>(`${API_URL}/auth/refresh`, {withCredentials: true})
            localStorage.setItem('token', response.data.accessToken);
            return $api.request(originalRequest);
        } catch (e) {
            console.log('НЕ АВТОРИЗОВАН')
        }
    }
    throw error;
})


export default $api;
