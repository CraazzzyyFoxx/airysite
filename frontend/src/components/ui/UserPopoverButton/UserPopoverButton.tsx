import React, {FC} from 'react';
import "./UserPopoverButton.css";

interface UserPopoverButtonProps {
    id?: string
    children: React.ReactChild | React.ReactNode
    style?: any
    onClick?: () => any
}

const UserPopoverButton: FC<UserPopoverButtonProps> = (props) => {
    return (
        <button className="user-popover-button" {...props}>
            {props.children}
        </button>
    );
};

export default UserPopoverButton;