import React, {FC} from 'react';
import {Popover} from "antd";
import "./UserPopover.css"

interface UserPopoverProps {
    id?: string
    content: any
    children: React.ReactChild | React.ReactNode
    style?: any
    onClick?: () => any
}

const UserPopover: FC<UserPopoverProps> = (props) => {
    return (
        <Popover placement="bottom" content={props.content}>
            {props.children}
        </Popover>
    );
};

export default UserPopover;