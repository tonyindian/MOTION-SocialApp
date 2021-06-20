import React from "react";
import logo from "../../../../Assets/pngs/logo.png";
import posts_logo from "../../../../Assets/pngs/posts_logo.png";
import friends_logo from "../../../../Assets/svgs/icon-friends.svg";
import notification from "../../../../Assets/svgs/notification_bell.svg";
import menu from "../../../../Assets/svgs/menu.svg";
import jennifer from "../../../../Assets/images/users/jennifer.png";
import { useHistory } from "react-router";
import {
  MBDiv,
  MenuLeft,
  LogoImg,
  MBTitle,
  PostsBtn,
  FriendsBtn,
  MenuRight,
  UserBtn,
  MenuBtn,
  BaseBtn,
} from "./styled.js";

const MenuBar = () => {
  const history = useHistory();

  const userBtnHandler = () => {
    history.push("/profile");
  };

  const postsBtnHandler = () => {
    history.push("/feed");
  };

  const friendsBtnHandler = () => {
    history.push("/friends");
  };

  return (
    <MBDiv>
      <MenuLeft>
        <LogoImg src={logo} />
        <MBTitle>Motion</MBTitle>
        <PostsBtn onClick={postsBtnHandler}>
          <img src={posts_logo} alt="posts" fill="red" stroke="green" />
          <p>Posts</p>
        </PostsBtn>
        <FriendsBtn onClick={friendsBtnHandler}>
          <img src={friends_logo} alt="friends" fill="red" stroke="green" />
          <p>Find Friends</p>
        </FriendsBtn>
      </MenuLeft>
      <MenuRight>
        <BaseBtn>
          <img src={notification} alt="alert-bell" />
        </BaseBtn>
        <UserBtn onClick={userBtnHandler}>
          <img src={jennifer} alt="user" />
        </UserBtn>
        <MenuBtn>
          <img src={menu} alt="menu-button" />
        </MenuBtn>
      </MenuRight>
    </MBDiv>
  );
};

export default MenuBar;
