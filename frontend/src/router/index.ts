import React from "react";
import Main from "../pages/Main";
import Dashboard from "../pages/Dashboard";

export interface IRoute {
    path: string;
    component: React.ComponentType;
    exact?: boolean;
}

export enum RouteNames {
    LOGIN = '/',
    DASHBOARD = '/dashboard'
}

export const publicRoutes: IRoute[] = [
    {path: RouteNames.LOGIN, exact: true, component: Main}
]

export const privateRoutes: IRoute[] = [
    {path: RouteNames.LOGIN, exact: true, component: Main},
    {path: RouteNames.DASHBOARD, exact: true, component: Dashboard}
]
