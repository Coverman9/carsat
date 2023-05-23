import React from "react";
import { NavLink } from "react-router-dom";
import { useSelector } from "react-redux";
import ProfileButton from "./ProfileButton";
import { Link } from "react-router-dom";
import "./Navigation.css";
import logo from "./carsat-logo.png";

function Navigation({ isLoaded }) {
  const sessionUser = useSelector((state) => state.session.user);

  return (
    <div className="main-navbar">
      <div className="logo-carsat">
        <NavLink exact to="/">
          <img className="carsat-logo" src={logo}/>
        </NavLink>
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
            <ProfileButton user={sessionUser} />
          </div>
        </>
      )}
    </div>
  );
}

export default Navigation;
