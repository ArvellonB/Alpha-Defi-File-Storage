// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DecentralizedFileStorage {
    // Struct to represent a stored file
    struct File {
        string name;
        string ipfsHash; // IPFS hash for file storage
        address owner;
        uint uploadTime;
        uint accessFee; // Fee to access the file
        bool isDeleted;
    }

    // Mapping from file ID to File struct
    mapping(uint => File) public files;
    // Mapping from user address to the list of owned file IDs
    mapping(address => uint[]) public userFiles;
    // Mapping to track how many times a file has been accessed
    mapping(uint => uint) public fileAccessCount;
    // Mapping to store file download history
    mapping(uint => address[]) public fileDownloadHistory;

    // Event emitted when a new file is uploaded
    event FileUploaded(uint indexed fileId, address indexed owner, string ipfsHash);
    // Event emitted when a file is accessed
    event FileAccessed(uint indexed fileId, address indexed user, uint feePaid);
    // Event emitted when a file is deleted
    event FileDeleted(uint indexed fileId, address indexed owner);
    // Event emitted when file ownership is transferred
    event OwnershipTransferred(uint indexed fileId, address indexed oldOwner, address indexed newOwner);

    // Counter for file IDs
    uint private fileIdCounter;

    constructor() {
        fileIdCounter = 1;
    }

    // Function to upload a file
    function uploadFile(string memory _name, string memory _ipfsHash, uint _accessFee) public {
        require(bytes(_name).length > 0, "File name is required");
        require(bytes(_ipfsHash).length > 0, "IPFS hash is required");
        
        // Create new file
        files[fileIdCounter] = File({
            name: _name,
            ipfsHash: _ipfsHash,
            owner: msg.sender,
            uploadTime: block.timestamp,
            accessFee: _accessFee,
            isDeleted: false
        });

        // Add file to the user's list
        userFiles[msg.sender].push(fileIdCounter);

        // Emit file uploaded event
        emit FileUploaded(fileIdCounter, msg.sender, _ipfsHash);

        // Increment file ID counter
        fileIdCounter++;
    }

    // Function to access a file (with fee payment)
    function accessFile(uint _fileId) public payable {
        File storage file = files[_fileId];
        require(!file.isDeleted, "File is deleted");
        require(msg.value >= file.accessFee, "Insufficient fee");

        // Increase file access count
        fileAccessCount[_fileId]++;

        // Record download history
        fileDownloadHistory[_fileId].push(msg.sender);

        // Transfer the fee to the file owner
        payable(file.owner).transfer(msg.value);

        // Emit file accessed event
        emit FileAccessed(_fileId, msg.sender, msg.value);
    }

    // Function to delete a file (only owner can delete)
    function deleteFile(uint _fileId) public {
        File storage file = files[_fileId];
        require(file.owner == msg.sender, "Only the owner can delete the file");

        // Mark file as deleted
        file.isDeleted = true;

        // Emit file deleted event
        emit FileDeleted(_fileId, msg.sender);
    }

    // Function to transfer ownership of a file
    function transferOwnership(uint _fileId, address _newOwner) public {
        File storage file = files[_fileId];
        require(file.owner == msg.sender, "Only the owner can transfer ownership");
        require(_newOwner != address(0), "Invalid new owner");

        // Transfer ownership
        address oldOwner = file.owner;
        file.owner = _newOwner;

        // Remove file from old owner's list
        _removeFileFromUser(msg.sender, _fileId);
        // Add file to new owner's list
        userFiles[_newOwner].push(_fileId);

        // Emit ownership transfer event
        emit OwnershipTransferred(_fileId, oldOwner, _newOwner);
    }

    // Internal function to remove file from user's list
    function _removeFileFromUser(address _user, uint _fileId) internal {
        uint[] storage fileList = userFiles[_user];
        for (uint i = 0; i < fileList.length; i++) {
            if (fileList[i] == _fileId) {
                fileList[i] = fileList[fileList.length - 1];
                fileList.pop();
                break;
            }
        }
    }

    // View function to get a user's files
    function getUserFiles(address _user) public view returns (uint[] memory) {
        return userFiles[_user];
    }

    // View function to get the download history of a file
    function getFileDownloadHistory(uint _fileId) public view returns (address[] memory) {
        return fileDownloadHistory[_fileId];
    }
}
