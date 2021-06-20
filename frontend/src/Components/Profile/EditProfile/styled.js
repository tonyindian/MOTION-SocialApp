import styled from "styled-components";
import { BaseButton } from "../../Verification/Base_Button/styled";

export const Wrapper = styled.div`
  width: 80%;
  height: 600px;
  min-width: 700px;
  margin-right: 10%;
  margin-left: 10%;
  display: flex;
  background-color: ${(props) => props.theme.backgroundWhite};
  box-shadow: 0px 10px 20px 0px ${(props) => props.theme.black05};
  box-shadow: 0px 0px 1px 0px ${(props) => props.theme.black20};
  position: relative;
  top: 130px;
`;

export const LeftContainer = styled.div`
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  width: 30%;
  min-width: 158px;
  border-right: 1px solid ${(props) => props.theme.black10};
`;
export const RightContainer = styled.div`
  width: 70%;
  margin: 0 5%;
`;

export const EditProfileButton = styled(BaseButton)`
  height: 40px;
  width: 158px;
  font-weight: ${(props) => props.theme.textWeightRegular};
  font-size: ${(props) => props.theme.textSizeXXS};
  margin-bottom: 10px;
  margin-top: 10px;

  :hover {
    cursor: pointer;
  }
`;

export const ProfilePictureWrapper = styled.img`
  margin-top: 20px;
  height: 80px;
  width: 80px;
`;
export const PersonalInformationWrapper = styled.div`
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 8%;
`;
export const UpdatePersonalInformation = styled.div`
  margin-top: 5%;
`;
export const WhatsonyourMind = styled.div`
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-content: center;
`;
export const UpdateButton = styled.button`
  background-color: ${(props) => props.theme.backgroundWhite};
  border: none;
  display: flex;
  justify-content: space-between;
  flex-direction: row;
  align-content: center;
  padding: 10px 20px;
  font-size: ${(props) => props.theme.textSizeS};
  :hover {
    cursor: pointer;
    background-color: ${(props) => props.theme.black05};
  }
`;
export const UpdateUserImage = styled.div`
  box-shadow: 0px 10px 20px 0px #0000000d;
  box-shadow: 0px 0px 1px 0px #00000033;
  border-radius: 4px;
  display: flex;
  justify-content: space-space-around;
  flex-direction: column;
  align-content: center;
`;
export const ImageWrapper = styled.img`
  opacity: 0.2;
  width: 14px;
  height: 18px;
  margin-right: 10px;
`;
export const CameraWrapper = styled(ImageWrapper)`
  opacity: 1;
  width: 14px;
  height: 18px;
  margin-right: 10px;
`;

export const SaveButton = styled(EditProfileButton)`
  background: ${(props) => props.theme.linearGradientGradButton};
  color: ${(props) => props.theme.backgroundWhite};
`;
export const InputLabelWrapper = styled.label`
  color: ${(props) => props.theme.black50};
  font-size: ${(props) => props.theme.textSizeXS};
`;
export const ThingsLiked = styled.button`
  font-size: ${(props) => props.theme.textSizeXXS};
  background: ${(props) => props.theme.black05};
  border: none;
  border-radius: 18px;
  padding: 8px 25px 8px 16px;
`;

export const LeftInformationWrapper = styled.div``;

export const RightInformationWrapper = styled.div``;

export const ThingsWrapper = styled.div`
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
  align-content: flex-start;
  font-size: ${(props) => props.theme.textSizeS};
`;
export const ThingsILikeTitle = styled.div`
  font-size: ${(props) => props.theme.textSizeS};
  padding: 20px 0px;
`;
export const DeleteIcon = styled.img`
  position: absolute;
  width: 10px;
  height: 10px;
  margin-left: 5px;
`;

export const FileUpload = styled.input`
  display: none;
`;
export const ChangeBackgroundImageBtn = styled(EditProfileButton)`
  border: none;
  font-size: 14px;
  position: absolute;
  top: -50px;
  right: 0px;
  color: white;
  opacity: 1;
`;
export const BottomButtons = styled.div`
  margin-top: 30%;
`;
