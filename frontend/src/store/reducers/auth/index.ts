import {AuthAction, IAuthState, AuthActionEnum} from "./types";

const initState: IAuthState = {
    // @ts-ignore
    user: null,
    isAuth: false
}


export default function AuthReducer(state = initState, action: AuthAction): IAuthState {
    switch (action.type) {
        case AuthActionEnum.SET_USER:
            return {...state, user: action.payload}
        case AuthActionEnum.SET_AUTH:
            return {...state, isAuth: action.payload}
        default:
            return state;
    }
}