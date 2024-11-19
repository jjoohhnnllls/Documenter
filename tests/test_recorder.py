import pytest
import cv2
import numpy as np
import os
import tempfile
from unittest.mock import Mock, patch
from src.backend.recorder.screen_recorder import ScreenRecorder

class TestScreenRecorder:
    @pytest.fixture
    def recorder(self):
        """Fixture to create a fresh ScreenRecorder instance for each test"""
        return ScreenRecorder()

    @pytest.fixture
    def temp_output_dir(self):
        """Fixture to create a temporary directory for video output"""
        with tempfile.TemporaryDirectory() as temp_dir:
            yield temp_dir

    def test_recorder_initialization(self, recorder):
        """Test if the recorder initializes with correct default values"""
        assert recorder.recording == False
        assert hasattr(recorder, 'output_path')
        assert hasattr(recorder, 'frame_rate')
        assert recorder.frame_rate > 0

    @patch('pyautogui.screenshot')
    def test_start_recording(self, mock_screenshot, recorder):
        """Test if recording starts properly"""
        # Mock screenshot to return a dummy image
        dummy_image = np.zeros((100, 100, 3), dtype=np.uint8)
        mock_screenshot.return_value = Mock(
            tobytes=lambda: dummy_image.tobytes(),
            size=(100, 100)
        )

        # Start recording
        recorder.start_recording()
        assert recorder.recording == True
        assert recorder.video_writer is not None

        # Cleanup
        recorder.stop_recording()

    def test_stop_recording(self, recorder, temp_output_dir):
        """Test if recording stops properly and saves the file"""
        output_path = os.path.join(temp_output_dir, 'test_recording.mp4')
        recorder.output_path = output_path

        # Start and immediately stop recording
        recorder.start_recording()
        recorder.stop_recording()

        assert recorder.recording == False
        assert recorder.video_writer is None

    @patch('pyautogui.screenshot')
    def test_capture_frame(self, mock_screenshot, recorder):
        """Test if frames are captured correctly"""
        # Create a dummy image
        dummy_image = np.zeros((100, 100, 3), dtype=np.uint8)
        mock_screenshot.return_value = Mock(
            tobytes=lambda: dummy_image.tobytes(),
            size=(100, 100)
        )

        frame = recorder._capture_frame()
        assert frame is not None
        assert isinstance(frame, np.ndarray)
        assert frame.shape == (100, 100, 3)

    def test_invalid_output_path(self, recorder):
        """Test handling of invalid output path"""
        recorder.output_path = "/invalid/path/video.mp4"
        
        with pytest.raises(Exception):
            recorder.start_recording()

    @pytest.mark.parametrize("frame_rate", [20, 30, 60])
    def test_different_frame_rates(self, frame_rate, recorder):
        """Test recording with different frame rates"""
        recorder.frame_rate = frame_rate
        recorder.start_recording()
        assert recorder.video_writer is not None
        assert recorder.video_writer.get(cv2.CAP_PROP_FPS) == frame_rate
        recorder.stop_recording()

    @patch('pyautogui.screenshot')
    def test_recording_duration(self, mock_screenshot, recorder, temp_output_dir):
        """Test recording for a specific duration"""
        import time

        # Mock screenshot to return a dummy image
        dummy_image = np.zeros((100, 100, 3), dtype=np.uint8)
        mock_screenshot.return_value = Mock(
            tobytes=lambda: dummy_image.tobytes(),
            size=(100, 100)
        )

        output_path = os.path.join(temp_output_dir, 'duration_test.mp4')
        recorder.output_path = output_path
        
        # Record for 1 second
        recorder.start_recording()
        time.sleep(1)
        recorder.stop_recording()

        # Check if file exists and has content
        assert os.path.exists(output_path)
        assert os.path.getsize(output_path) > 0

    def test_pause_resume_recording(self, recorder):
        """Test pausing and resuming recording if implemented"""
        if hasattr(recorder, 'pause_recording'):
            recorder.start_recording()
            recorder.pause_recording()
            assert recorder.paused == True
            recorder.resume_recording()
            assert recorder.paused == False
            recorder.stop_recording()

    @patch('pyautogui.screenshot')
    def test_memory_cleanup(self, mock_screenshot, recorder):
        """Test if resources are properly cleaned up after recording"""
        dummy_image = np.zeros((100, 100, 3), dtype=np.uint8)
        mock_screenshot.return_value = Mock(
            tobytes=lambda: dummy_image.tobytes(),
            size=(100, 100)
        )

        recorder.start_recording()
        recorder.stop_recording()

        assert recorder.video_writer is None
        # Add more cleanup checks based on your implementation

    def test_concurrent_recording_prevention(self, recorder):
        """Test that we can't start a second recording while one is in progress"""
        recorder.start_recording()
        
        with pytest.raises(Exception):
            recorder.start_recording()

        recorder.stop_recording()

if __name__ == '__main__':
    pytest.main([__file__])