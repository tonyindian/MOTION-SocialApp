import styled from "styled-components";

export const MBDiv = styled.div`
  display: flex;
  width: 100%;
  height: 80px;
  justify-content: space-between;
  background: #ffffff;
  z-index: 1;
  box-shadow: 0px 0px 1px rgba(0, 0, 0, 0.2), 0px 10px 20px rgba(0, 0, 0, 0.05);
  border-bottom: 1px solid rgba(0, 0, 1, 0.09);
`;

export const MenuLeft = styled.div`
  display: flex;
  justify-content: flex-start;
  padding-left: 3%;
  align-items: center;
  width: 70%;
`;

export const BaseBtn = styled.button`
  background: none;
  border: none;
  height: 100%;
  border-bottom: 2px solid transparent;

  :hover {
    border-bottom: 2px solid #ad73fd;
    height: 103.5%;
  }
`;

export const MenuRight = styled.div`
  display: flex;
  justify-content: flex-end;
  padding-right: 3%;
  align-items: center;
  width: 30%;
`;

export const LogoImg = styled.img`
  height: 26px;
  width: 26px;
`;

export const MBTitle = styled.p`
  font-size: ${(props) => props.theme.textSizeTitle};
  margin-left: 2%;
  margin-right: 8%;
`;

export const BasePFBtn = styled(BaseBtn)`
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 103.5%;
  font-size: ${(props) => props.theme.textSizeDefault};

  :hover {
    border-bottom: 2px solid #ad73fd;
    height: 103.5%;
  }
`;

export const PostsBtn = styled(BasePFBtn)`
  width: 80px;
  margin-right: 6%;
`;

export const FriendsBtn = styled(BasePFBtn)`
  width: 129px;
`;

export const MenuBtn = styled(BaseBtn)`
  width: 20px;
  height: 100%;
  margin-left: 5%;
`;

export const UserBtn = styled(BaseBtn)`
  width: 50px;
  margin-left: 15%;
  height: 100%;
`;

export const ProfilePicture = styled.img`
  height: 50px;
  width: 50px;
`
