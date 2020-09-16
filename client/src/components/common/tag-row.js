import React from "react";
import { categoryColors } from "./styles";

export default function TagRow({ tags }) {
  return (
    <div className="tags__container">
      {tags.map((tag, idx) => (
        <span
          key={idx}
          className="tag"
          style={{ backgroundColor: categoryColors[tag] }}
        >
          {tag.toLowerCase()}
        </span>
      ))}
    </div>
  );
}
