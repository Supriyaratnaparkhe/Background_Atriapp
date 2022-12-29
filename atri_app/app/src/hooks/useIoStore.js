import create from "zustand";

const useIoStore = create((set) => {
  return {
  "Home": {
    "Upload1": {
      "io": {
        "files": {
          "type": "files",
          "mode": "upload"
        }
      }
    },
    "Upload3": {
      "io": {
        "files": {
          "type": "files",
          "mode": "upload"
        }
      }
    }
  }
}});

export default useIoStore;
