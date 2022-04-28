import React from 'react';
import "./StatsTitle.css";

import {Row, Col } from "antd"

const StatsTitle = () => {
    return (
        <div className="container-fluid">
            <div className="stats-title">
                <Row >
                    <Col span={12}>
                        <img src={"button.png"} alt={"button"} className="btn-img"/>
                    </Col>
                    <Col span={12}>
                    <img src={"button.png"} alt={"button"} className="btn-img"/>
                    </Col>
                </Row>
            </div>
        </div>
    );
};

export default StatsTitle;