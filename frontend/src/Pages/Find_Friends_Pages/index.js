import styled from "styled-components";
import MenuBar from "../../Components/Feed_components/Header/Menu_Bar";
import Main from "../../Components/Verification/Main Wrapper";
import Person from "../../Components/Friends_components/Person";
import { useEffect, useState } from "react";
import Axios from "../../API";
import { useSelector } from "react-redux";
import Masonry from "react-masonry-css";
import { v4 as uuidv4 } from "uuid";
import "./styles.css";

export const FeedMain = styled(Main)`
  display: flex;
  flex-direction: column;
  background-color: ${(props) => props.theme.postsBackground};
  height: auto;
`;

const FindFriends = () => {
  const token = useSelector((state) => state.token);
  const [userList, setUserList] = useState([]);

  useEffect(() => {
    async function fetchUsers() {
      const limit = 100;
      const offset = 0;
      const url = `users/?limit=${limit}&offset=${offset}`;
      const config = {
        headers: { Authorization: `Bearer ${token}` },
      };
      try {
        const resp = await Axios.get(url, config);
        if (resp.status === 200) {
          setUserList(resp.data.results);
        }
      } catch (err) {
        if (err.response.status === 400) {
          console.log(err.response);
        }
      }
    }
    fetchUsers();
  }, [token]);

  return (
    <FeedMain>
      <MenuBar />
      <Masonry
        breakpointCols={4}
        className="my-masonry-grid"
        columnClassName="my-masonry-grid_column"
      >
        {userList.map((user) => (
          <Person user={user} key={uuidv4()} />
        ))}
      </Masonry>
    </FeedMain>
  );
};

export default FindFriends;
