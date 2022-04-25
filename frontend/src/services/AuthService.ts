import $api from "../http";
import {API_URL} from "../consts/API";

export default class AuthService {
    static async login(){
        window.open(`${API_URL}/auth/login`, "_self")
    }

    static async logout(): Promise<void> {
        return $api.post('/auth/logout')
    }


}

