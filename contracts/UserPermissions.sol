pragma solidity >=0.4.22 <0.9.0;

contract UserPermissions {
    mapping(address => mapping(address => bool)) public permissions;

    function setPermissions(address _sender, address _they, bool _allowed) public {
         permissions[_sender][_they] = _allowed;
    }

    function getPermitted(address sender, address they) public view returns(bool) {
        return permissions[they][sender];
    }
}