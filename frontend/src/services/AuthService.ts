import $api from "../http";
import {API_URL} from "../consts/API";
import {AuthActionEnum} from "../store/reducers/auth/types";
import {useDispatch} from "react-redux";

export default class AuthService {
    static async login(){
        window.open(`${API_URL}/auth/login`, "_self")
    }

    static async logout(): Promise<void> {
        return $api.post('/auth/logout')
    }


}

