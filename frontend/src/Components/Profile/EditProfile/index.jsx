import Profilpicture from "../../../Assets/images/users/patricia.png"
import{ Wrapper, LeftContainer, RightContainer, ProfilePictureWrapper,EditProfileButton, UpdateUserImage, UpdateButton, ImageWrapper, SaveButton} from "./styled"
import{ ThingsLiked, UpdatePersonalInformation, PersonalInformationWrapper, LeftInformationWrapper, InputLabelWrapper, RightInformationWrapper, ThingsWrapper, WhatsonyourMind} from "./styled"
import BaseInput from "../../../Components/Verification/Base_Input";
import RemoveBin from "../../../Assets/svgs/remove_bin.svg"
import UploadArrow from "../../../Assets/svgs/upload_arrow.svg"
import React from "react";
import { useState } from "react";
import {useSelector } from "react-redux"


const EditProfileWrapper = () => {
    const user = useSelector((state)=>state.user);
    const templateUser = {...user};
    const [isOpen, setIsOpen] = useState(false);

    const setOpen = () =>{
        setIsOpen(!isOpen);
    }

    const onChangeHandler = (e) =>{
        templateUser[e.target.id] = e.target.value;   
    }

    const submitChanges = () =>{
        //dispatch to change userinfo 
    }

    const UploadNewAvatar = (e) =>{
        // URL.createObjectURL(e.target.files);
    }

    return(
        <Wrapper>
        <LeftContainer>
            <ProfilePictureWrapper src={Profilpicture}></ProfilePictureWrapper>
            <EditProfileButton onClick={setOpen}>UPDATE IMAGE</EditProfileButton>
            {isOpen && <UpdateUserImage>
                <UpdateButton onClick={UploadNewAvatar}><ImageWrapper src={UploadArrow}></ImageWrapper>Upload </UpdateButton>
                <UpdateButton><ImageWrapper src={RemoveBin}></ImageWrapper>Remove</UpdateButton>
            </UpdateUserImage>}
            <EditProfileButton >DELETE ACCOUNT</EditProfileButton>
            <SaveButton onClick ={submitChanges}>SAVE</SaveButton>
        </LeftContainer>
        <RightContainer>
            <UpdatePersonalInformation>
                <PersonalInformationWrapper>
                    <LeftInformationWrapper>
                        <InputLabelWrapper>First name</InputLabelWrapper>
                        <BaseInput name={user.first_name} type="text" id="first_name" onChange={onChangeHandler} ></BaseInput>
                        <InputLabelWrapper>Email</InputLabelWrapper>
                        <BaseInput name={user.email} type="text" id="email" onChange={onChangeHandler} ></BaseInput>
                        <InputLabelWrapper>Location</InputLabelWrapper>
                        <BaseInput name={user.location} type="text" id="location" onChange={onChangeHandler} ></BaseInput>
                        <InputLabelWrapper>About</InputLabelWrapper>
                        <BaseInput name={user.about_me} type="text" id="about_me" onChange={onChangeHandler} ></BaseInput>
                    </LeftInformationWrapper>
                    <RightInformationWrapper>
                        <InputLabelWrapper>Last name</InputLabelWrapper>
                        <BaseInput name={user.last_name} type="text" id="last_name" onChange={onChangeHandler} ></BaseInput>
                        <InputLabelWrapper>Username</InputLabelWrapper>
                        <BaseInput name={user.username} type="text" id="username" onChange={onChangeHandler} ></BaseInput>
                        <InputLabelWrapper>Phone</InputLabelWrapper>
                        <BaseInput name="PhoneNumber" type="text" id="phone" onChange={onChangeHandler} ></BaseInput>
                        <InputLabelWrapper>Password</InputLabelWrapper>
                        <BaseInput type="password" id="password" onChange={onChangeHandler} ></BaseInput>
                    </RightInformationWrapper>
                </PersonalInformationWrapper>
                <ThingsWrapper>
                    {user.things_user_likes.length > 0 ? user.things_user_likes.map(item => <ThingsLiked key={item}>{item}</ThingsLiked>) : null}                
                </ThingsWrapper>
                <WhatsonyourMind>
                    <BaseInput name="Type something..."></BaseInput>
                    <EditProfileButton >ADD</EditProfileButton>
                </WhatsonyourMind>
            </UpdatePersonalInformation>
        </RightContainer>
    </Wrapper>
    )
}
export default EditProfileWrapper;