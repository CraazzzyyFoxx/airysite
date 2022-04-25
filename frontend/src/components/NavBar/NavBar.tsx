import React, {FC} from 'react';
import {Layout, Menu, Row, Button} from "antd";
import classes from './NavBar.module.css';
import AuthService from "../../services/AuthService";
import {useDispatch} from "react-redux";
import {useTypedSelector} from "../../hooks/useTypedSelector";
import {AuthActionEnum} from "../../store/reducers/auth/types";



const Navbar: FC = () => {
    const dispatch = useDispatch()
    const {user} = useTypedSelector(state => state.auth)

    async function logout () {
        await AuthService.logout()
        dispatch({type: AuthActionEnum.SET_USER, payload: null})
        dispatch({type: AuthActionEnum.SET_AUTH, payload: false})
    }

    return (
        <Layout.Header>
            <Row>
                <div className={classes.logo}>
                    <img src="logo.png" alt={"logo"}/>
                </div>
                    <h1 style={{marginLeft: "20px"}}>Airy</h1>
                    {/*{user ?*/}
                    {/*    (<div>*/}
                    {/*        <img src={`https://cdn.discordapp.com/avatars/${user.id}/${user.avatar_hash}.png?size=4096`}*/}
                    {/*             alt="" className={classes.avatar}/>*/}
                    {/*        {user.username}*/}
                    {/*        <Button style={{marginLeft: "20px"}} onClick={logout}>Logout</Button>*/}
                    {/*    </div>*/}
                    {/*    )*/}
                    {/*    :*/}
                    {/*    (*/}
                    {/*        <Button type="primary" shape="round" size={"large"}>*/}
                    {/*            Login*/}
                    {/*        </Button>*/}
                    {/*    )*/}
                    {/*    }*/}
            </Row>
        </Layout.Header>
    );
};

export default Navbar;
