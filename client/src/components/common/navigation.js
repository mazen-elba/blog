import React, { useState } from "react";
import { Link } from "react-router-dom";

import { Avatar } from "antd";

const navLinks = [
  {
    title: "Home",
    path: "/",
  },
  {
    title: "Blogs",
    path: "/blogs",
  },
  {
    title: "Contacts",
    path: "/contacts",
  },
  {
    title: "Login",
    path: "/login",
  },
];

export default function Navigation({ user }) {
  const [menuActive, setMenuActive] = useState(false);

  return (
    <nav className="site__navigation">
      <span className="menu__title">MAiA Blog</span>
      <div className={`menu__content__container ${menuActive && "active"}`}>
        <ul>
          {navLinks.map((link, index) => (
            <li key={index}>
              <Link to={link.path}>{link.title}</Link>
            </li>
          ))}
        </ul>
        <span className="menu__avatar__container">
          <Avatar
            src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
            size={38}
          />
          <span className="menu__avatar__name">{`${user.firstName} ${user.lastName}`}</span>
        </span>
      </div>
      <i
        className="ionicons icon ion__ios__menu"
        onClick={() => setMenuActive(!menuActive)}
      />
    </nav>
  );
}
