import React, {FC} from 'react';
import {Layout, Anchor, Row, Col, Button} from "antd";
import AuthService from "../../services/AuthService";
import {useTypedSelector} from "../../hooks/useTypedSelector";

import './AppHeader.css';
import GreenButton from "../ui/GreenButton/GreenButton";
import UserMenu from "../UserMenu/UserMenu";

const AppHeader: FC = () => {
    const {user, isAuth} = useTypedSelector(state => state.auth)

    return (
        <Layout.Header className="app-header">
            <div className="logo">
                <img className="logo" src="logo.png" alt={"logo"}/>
                <a href="https://google.com" style={{color: "white"}}>Airy</a>
            </div>
            <div>
                <Row gutter={[16, 16]}>
                    <Col  className="mobileHidden"><a>Plugins</a></Col>
                    <Col  className="mobileHidden"><a>Documentation</a></Col>
                    <Col  className="mobileHidden"><a href={"https://discord.gg/F4WwGCtMtR"}>Support Server</a></Col>
                    {
                        isAuth ?
                            <>
                                <UserMenu/>
                            </>
                            :
                            <Col><GreenButton onClick={AuthService.login}>Login</GreenButton></Col>
                    }
                </Row>

            </div>
        </Layout.Header>
    );
};

export default AppHeader;
