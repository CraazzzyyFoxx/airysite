import './App.css';

import React, {useEffect} from 'react';
import AppHeader from "./components/AppHeader/AppHeader";
import {User} from "./models/User";
import $api from "./http";
import {useDispatch} from "react-redux";
import {AuthActionEnum} from "./store/reducers/auth/types";
import {Layout} from "antd";
import TitleSlide from "./components/TitleSlide/TitleSlide";
import AppFooter from "./components/AppFooter/AppFooter";

const {Content} = Layout;

function App() {
    const dispatch = useDispatch()
    const getUser = async () => {
        let resp = await $api.post<User>('/user/')
        resp = {...resp, }
        dispatch({type: AuthActionEnum.SET_USER, payload: resp.data})
        dispatch({type: AuthActionEnum.SET_AUTH, payload: true})
    };

    useEffect(() => {getUser()}, []);


  return (
      <Layout className="layout">
          <AppHeader/>
          <br/>
          <br/>
          <Content>
              <div className="site-layout-content">
                  <TitleSlide/>
              </div>
          </Content>
          <AppFooter/>
      </Layout>
  );
}

export default App;
