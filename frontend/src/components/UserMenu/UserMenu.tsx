import React from 'react';
import {Avatar,  Popover} from 'antd';
import {useTypedSelector} from "../../hooks/useTypedSelector";
import "./Usermenu.css";
import UserPopover from "../ui/UserPopover/UserPopover";
import UserPopoverButton from "../ui/UserPopoverButton/UserPopoverButton";
import AuthService from "../../services/AuthService";
import {useDispatch} from "react-redux";
import {AuthActionEnum} from "../../store/reducers/auth/types";


const UserMenu = () => {
    const dispatch = useDispatch()

    async function logout () {
        await AuthService.logout()
        dispatch({type: AuthActionEnum.SET_USER, payload: null})
        dispatch({type: AuthActionEnum.SET_AUTH, payload: false})
    }

    const content = (
        <div>
            <UserPopoverButton>My Servers</UserPopoverButton>
            <br/>
            <UserPopoverButton style={{color: "#7E2530"}} onClick={logout}>Logout</UserPopoverButton>
        </div>
    );

    const {user} = useTypedSelector(state => state.auth)

    return (
        <div className="user-menu">
            <Avatar src={`https://cdn.discordapp.com/avatars/${user.id}/${user.avatar_hash}.png?size=4096`}/>
            <UserPopover content={content}>
                    <span>{user.username}</span>
            </UserPopover>
        </div>
    );
};

export default UserMenu;