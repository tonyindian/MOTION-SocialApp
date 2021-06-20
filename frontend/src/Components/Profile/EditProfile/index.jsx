import {
  Wrapper,
  LeftContainer,
  RightContainer,
  ProfilePictureWrapper,
  EditProfileButton,
  UpdateUserImage,
  UpdateButton,
  ImageWrapper,
  SaveButton,
} from "./styled";
import {
  CameraWrapper,
  BottomButtons,
  ChangeBackgroundImageBtn,
  FileUpload,
  ThingsLiked,
  DeleteIcon,
  ThingsILikeTitle,
  UpdatePersonalInformation,
  PersonalInformationWrapper,
  LeftInformationWrapper,
  InputLabelWrapper,
  RightInformationWrapper,
  ThingsWrapper,
  WhatsonyourMind,
} from "./styled";
import BaseInput from "../../../Components/Verification/Base_Input";
import RemoveBin from "../../../Assets/svgs/remove_bin.svg";
import UploadArrow from "../../../Assets/svgs/upload_arrow.svg";
import React from "react";
import { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import CrossIcon from "../../../Assets/svgs/cross_icon.svg";
import Axios from "../../../API/index.js";
import { useHistory } from "react-router-dom";
import Camera from "../../../Assets/svgs/camera.svg";
import standardAvatar from "../../../Assets/pngs/generic_user.png";

const EditProfileWrapper = () => {
  const history = useHistory();
  const user = useSelector((state) => state.user);
  const token = useSelector((state) => state.token);

  const [isOpen, setIsOpen] = useState(false);
  const [addThing, setAddthing] = useState("");
  const [templateUser, setTemplateUser] = useState({ ...user });

  const dispatch = useDispatch();
  const setOpen = () => {
    setIsOpen(!isOpen);
  };

  const onChangeHandler = (e) => {
    const value = e.target.value;
    const input = e.target.id;
    setTemplateUser({ ...templateUser, [input]: value });
  };

  const submitChanges = async () => {
    const url = "users/me/";
    const body = {
      email: templateUser.email,
      first_name: templateUser.first_name,
      last_name: templateUser.last_name,
      username: templateUser.username,
      location: templateUser.location,
      about_me: templateUser.about_me,
      things_user_likes: templateUser.things_user_likes,
    };
    const config = {
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      },
    };
    try {
      const resp = await Axios.patch(url, body, config);
      if (resp.status === 200) {
        history.push("/profile");
      }
    } catch (err) {
      if (err.response.status === 400) {
        console.log(err.response);
      }
    }
  };

  const updateImage = async (e) => {
    const url = "users/me/";

    const data = new FormData();

    if (e.target.name === "remove") {
      const response = await fetch(standardAvatar);
      const blob = await response.blob();
      const file = new File([blob], "image.jpg", { type: blob.type });
      data.append("avatar", file);
    } else {
      data.append(e.target.name, e.target.files[0]);
    }

    const config = {
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "multipart/form-data",
      },
    };
    try {
      const resp = await Axios.patch(url, data, config);
      if (resp.status === 200) {
        dispatch({ type: "FETCHPROFILE", payload: resp.data });
      }
    } catch (err) {
      if (err.response.status === 400) {
        console.log(err.response);
      }
    }
  };

  const DeleteLikedThing = (e) => {
    const tempUser = { ...templateUser };
    const index_delete = tempUser.things_user_likes.indexOf(e.target.id);
    tempUser.things_user_likes.splice(index_delete, 1);
    setTemplateUser({
      ...templateUser,
      things_user_likes: tempUser.things_user_likes,
    });
  };

  const AddThingILike = (e) => {
    setTemplateUser({
      ...templateUser,
      things_user_likes: [...templateUser.things_user_likes, addThing],
    });
  };
  const handleInputChanged = (e) => {
    setAddthing(e.target.value);
  };

  const deleteUser = async (e) => {
    const url = "users/me/";

    const config = {
      method: "DELETE",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    };
    await Axios.delete(url, config);
    history.push("/signup");
  };

  return (
    <Wrapper>
      <ChangeBackgroundImageBtn onChange={updateImage}>
        <CameraWrapper src={Camera}></CameraWrapper>
        <label class="custom-file-upload">
          <FileUpload name="banner" type="file" accept="image/png, image/jpg" />
          Update Image
        </label>
      </ChangeBackgroundImageBtn>
      <LeftContainer>
        <ProfilePictureWrapper src={user.avatar}></ProfilePictureWrapper>
        <EditProfileButton onClick={setOpen}>UPDATE IMAGE</EditProfileButton>
        {isOpen && (
          <UpdateUserImage>
            <UpdateButton id={"avatar"} onChange={updateImage}>
              <ImageWrapper src={UploadArrow}></ImageWrapper>
              <label class="custom-file-upload">
                <FileUpload
                  name="avatar"
                  type="file"
                  accept="image/png, image/jpg"
                />
                Upload
              </label>
            </UpdateButton>
            <UpdateButton name="remove" onClick={updateImage}>
              <ImageWrapper src={RemoveBin}></ImageWrapper>Remove
            </UpdateButton>
          </UpdateUserImage>
        )}
        <BottomButtons>
          <EditProfileButton onClick={deleteUser}>
            DELETE ACCOUNT
          </EditProfileButton>
          <SaveButton onClick={submitChanges}>SAVE</SaveButton>
        </BottomButtons>
      </LeftContainer>
      <RightContainer>
        <UpdatePersonalInformation>
          <PersonalInformationWrapper>
            <LeftInformationWrapper>
              <InputLabelWrapper>First name</InputLabelWrapper>
              <BaseInput
                name={user.first_name}
                type="text"
                id="first_name"
                onChange={onChangeHandler}
              ></BaseInput>
              <InputLabelWrapper>Email</InputLabelWrapper>
              <BaseInput
                name={user.email}
                type="text"
                id="email"
                onChange={onChangeHandler}
              ></BaseInput>
              <InputLabelWrapper>Location</InputLabelWrapper>
              <BaseInput
                name={user.location}
                type="text"
                id="location"
                onChange={onChangeHandler}
              ></BaseInput>
              <InputLabelWrapper>About</InputLabelWrapper>
              <BaseInput
                name={user.about_me}
                type="text"
                id="about_me"
                onChange={onChangeHandler}
              ></BaseInput>
            </LeftInformationWrapper>
            <RightInformationWrapper>
              <InputLabelWrapper>Last name</InputLabelWrapper>
              <BaseInput
                name={user.last_name}
                type="text"
                id="last_name"
                onChange={onChangeHandler}
              ></BaseInput>
              <InputLabelWrapper>Username</InputLabelWrapper>
              <BaseInput
                name={user.username}
                type="text"
                id="username"
                onChange={onChangeHandler}
              ></BaseInput>
              <InputLabelWrapper>Phone</InputLabelWrapper>
              <BaseInput
                name="123-456-789"
                type="text"
                id="phone"
                onChange={onChangeHandler}
              ></BaseInput>
              <InputLabelWrapper>Password</InputLabelWrapper>
              <BaseInput
                type="password"
                id="password"
                onChange={onChangeHandler}
              ></BaseInput>
            </RightInformationWrapper>
          </PersonalInformationWrapper>
          <ThingsILikeTitle>Things I like</ThingsILikeTitle>
          <ThingsWrapper>
            {templateUser.things_user_likes.length > 0 ? (
              templateUser.things_user_likes.map((item) => (
                <ThingsLiked key={item}>
                  {item}
                  <DeleteIcon
                    id={item}
                    src={CrossIcon}
                    onClick={DeleteLikedThing}
                  />
                </ThingsLiked>
              ))
            ) : (
              <ThingsLiked>
                Motion
                <DeleteIcon
                  id={"Motion"}
                  src={CrossIcon}
                  onClick={DeleteLikedThing}
                />
              </ThingsLiked>
            )}
          </ThingsWrapper>
          <WhatsonyourMind>
            <BaseInput
              name="Type something..."
              onChange={handleInputChanged}
            ></BaseInput>
            <EditProfileButton onClick={AddThingILike}>ADD</EditProfileButton>
          </WhatsonyourMind>
        </UpdatePersonalInformation>
      </RightContainer>
    </Wrapper>
  );
};
export default EditProfileWrapper;
