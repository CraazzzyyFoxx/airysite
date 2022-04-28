import React from 'react';
import {Footer} from "antd/es/layout/layout";
import "./AppFooter.css"
import {Col, Row} from "antd";
import UserMenu from "../UserMenu/UserMenu";
import GreenButton from "../ui/GreenButton/GreenButton";
import AuthService from "../../services/AuthService";

const AppFooter = () => {
    return (
        <Footer>
            <div style={{display: "flex", flexDirection: "column"}}>
                <div className="logo">
                    <img className="logo" src="logo.png" alt={"logo"}/>
                    <a href="https://google.com" style={{color: "white"}}>Airy</a>
                </div>
                <div className="footer-text">The best Discord bot, with which you can confidently improve and develop your server</div>
                <br/>
                <br/>

                <div className="footer-copyright">Copyright © 2022 Airy Development</div>
            </div>
            <div>
                <Row gutter={[24, 24]} style={{display: "flex"}}>
                    <Col><div className="col-header">Plugins</div></Col>
                    <Col><div className="col-header">Documentation</div></Col>
                    <Col><div className="col-header">Support Server</div></Col>
                </Row>
            </div>
        </Footer>
    );
};

export default AppFooter;