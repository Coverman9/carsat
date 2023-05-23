import React from "react";
import { NavLink } from "react-router-dom";
import { useSelector } from "react-redux";
import ProfileButton from "./ProfileButton";
import { Link } from "react-router-dom";
import "./Navigation.css";

function Navigation({ isLoaded }) {
  const sessionUser = useSelector((state) => state.session.user);

  return (
    <div className="main-navbar">
        <div>
          <li>
            <NavLink exact to="/">
              Home
            </NavLink>
          </li>
        </div>
        {isLoaded && (
          <>
            <div className="navbar-profile-buttons">
              {sessionUser && (
                <>
                  <Link to={`/profile/${sessionUser.id}`}>
                    <button className="profile-button">Profile</button>
                  </Link>
                  <Link to="/cars/new">
                    <button className="addcar-button">Add a Car</button>
                  </Link>
                </>
              )}
            </div>
            <div>
              <li>
                <ProfileButton user={sessionUser} />
              </li>
            </div>
          </>
        )}
    </div>
  );
}

export default Navigation;
