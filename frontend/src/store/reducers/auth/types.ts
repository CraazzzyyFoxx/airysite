import {User} from "../../../models/User";

export interface IAuthState {
    user: User
    isAuth: boolean
}

export enum AuthActionEnum {
    SET_USER = "SET_USER",
    SET_AUTH = "SET_AUTH"
}

export interface SetUserAction {
    type: AuthActionEnum.SET_USER
    payload: User
}

export interface SetIsAuthAction {
    type: AuthActionEnum.SET_AUTH
    payload: boolean
}

export type AuthAction = SetUserAction | SetIsAuthAction