import React from 'react';
import { Menu, MenuProps } from 'antd';
import {useTypedSelector} from "../../hooks/useTypedSelector";
import Icon from '@ant-design/icons';
import { AppstoreOutlined, MailOutlined, SettingOutlined } from '@ant-design/icons';

type MenuItem = Required<MenuProps>['items'][number];

function getItem(
    key: React.Key,
    icon?: React.ReactNode,
    children?: MenuItem[],
    type?: 'group',
): MenuItem {
    return {
        key,
        icon,
        children,
        type,
    } as MenuItem;
}


const UserMenu = () => {
    const {user} = useTypedSelector(state => state.auth)


    const UserIcon = (props: any) => <Icon component={<svg>{`https://cdn.discordapp.com/avatars/${user.id}/${user.avatar_hash}.svg?size=4096`}</svg>} {...props} />;

    const items: MenuProps['items'] = [
        getItem('Navigation One', <MailOutlined/>, [
            getItem('Item 1', null, [getItem('Option 1', '1'), getItem('Option 2', '2')], 'group'),
        ])];

    const onClick: MenuProps['onClick'] = e => {
        console.log('click ', e);
    };

    return (
        <Menu
            onClick={onClick}
            style={{ width: 256 }}
            defaultSelectedKeys={['1']}
            defaultOpenKeys={['sub1']}
            mode="inline"
            items={items}
        />
    );
};

export default UserMenu;